#!/usr/bin/python3
# config:utf-8


import smbus
import time

LCD_ADDR = 0x3e

LCD_SET_DDRAM_ADDR = 0x80

class i2cLcd:
	i2c = ""
	addr = ""
	reg_setting = 0x00
	reg_display = 0x40
	col_num = 16
	row_num = 2

	def __init__(self,bus_num,addr):
		self.addr = addr
		self.i2c = smbus.SMBus(bus_num)
		# LCD init
		self.i2c.write_i2c_block_data( self.addr, self.reg_setting, [0x38, 0x39, 0x14, 0x70, 0x56, 0x6c] )
		self.i2c.write_i2c_block_data( self.addr, self.reg_setting, [0x38, 0x0c, 0x01] )

	def __del__(self):
		self.clear_display()

	def setCursor(self,col,row):
		row_offset = [0x00,0x40]
		self.i2c.write_byte_data( self.addr, self.reg_setting, LCD_SET_DDRAM_ADDR | (col + row_offset[row]) )

	def write_scroll(self,str):
		#str_copy = str
		length = len(str)
		counter = 0
		#self.setCursor(0,0)
		self.write(str[counter:self.col_num+counter])
		time.sleep(1)
		counter += 1
		while length >= counter:
			self.clear_display()
			self.setCursor(0,0)
			self.write(str[counter:self.col_num+counter])
			time.sleep(0.4)
			counter += 1;
		#print("End")
	
	def write_smart(self,str):
		self.setCursor(0,0)
		length = len(str)
		if length > self.col_num*self.row_num:
			self.write_scroll(str)
		else:
			self.write(str)

	def write(self, str):
		counter = 0
		row = 1
		for c in list(str):
			self.i2c.write_byte_data( self.addr, self.reg_display, ord(c) )
			counter += 1
			if counter >= (self.col_num*self.row_num):
				break
			elif counter >= (self.col_num*row):
				self.setCursor(0,row)
				row += 1
				if row > self.row_num:
					break

	def clear_display(self):
		self.i2c.write_byte_data(self.addr,self.reg_setting,0x01)


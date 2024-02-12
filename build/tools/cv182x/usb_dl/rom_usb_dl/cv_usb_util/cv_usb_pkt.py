#!/usr/local/bin/python

# ========================================================================
# Define
# ========================================================================
rom_vidpid = 'VID:PID=3346:1000'
rom_cvi_vidpid = 'VID:PID=3346:1000'
prg_vidpid = 'VID:PID=30B1:1000'
uboot_vidpid = 'VID:PID=30B1:1001'
uboot_cvi_vidpid = 'VID:PID=3346:1001'
verify_vidpid = 'VID:PID='
kernel_acm_vidpid = 'VID:PID=30B1:1003'
kernel_libusb_vidpid = 'VID:PID=30B1:1003'

SUCCESS = 0
FAIL = 1

HEADER_SIZE = 8

CVI_USB_TX_DATA_TO_SRAM = 0
CVI_USB_TX_DATA_TO_DRAM = 1
CV_USB_NONE = 0
CV_USB_INFO = 1
CV_USB_BREAK = 2
CV_USB_KEEP_DL = 3
CV_USB_UBREAK = 4
CV_USB_PRG_CMD = 6
CVI_USB_REBOOT = 22
CVI_USB_PROGRAME = 0x83

# Cannot be too larger in Windows!
USB_BULK_MAX_SIZE = 0x80000  # 0x4000000

MSG_TOKEN_OFFSET = 0

RSP_CRC16_HI_OFFSET = 2
RSP_CRC16_LO_OFFSET = 3
RSP_TOKEN_OFFSET = 6

DUMMY_ADDR = 0xFF
TPU_SRAM_FIP_ADDR = 0x0C012000
DDR_FIP_ADDR = 0x80800000
HEADER_ADDR = 0x80080000
IMG_ADDR = 0x80090000

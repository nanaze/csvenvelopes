import sys
import cairo
import csvenv

def main():
  to_addresses = [
    '555 Test St\nSan Francisco CA',
    '145 Test St\nSan Francisco CA'
  ]
  from_address = '123 Test St\nSan Francisco CA'

  POINTS_PER_INCH = 72
  WIDTH_IN = 7
  HEIGHT_IN = 4

  WIDTH = WIDTH_IN * POINTS_PER_INCH
  HEIGHT = HEIGHT_IN * POINTS_PER_INCH
  
  surface = cairo.PDFSurface(sys.stdout, WIDTH, HEIGHT)
  csvenv.WriteEnvelopes(surface, to_addresses, from_address)
  
  
if __name__ == '__main__':
  main()

import sys
import cairo
import csvenv

def main():

  POINTS_PER_INCH = 72
  WIDTH_IN = 7
  HEIGHT_IN = 5

  WIDTH = WIDTH_IN * POINTS_PER_INCH
  HEIGHT = HEIGHT_IN * POINTS_PER_INCH
  
  surface = cairo.PDFSurface(sys.stdout, WIDTH, HEIGHT)

  for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
      
    csvenv.WriteEnvelope(surface, parts)
    
    surface.show_page()
    
  
  
if __name__ == '__main__':
  main()

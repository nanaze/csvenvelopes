import cairo

def _WriteLines(ctx, lines, font_size, line_spacing=2):

  x, y = ctx.get_current_point()
  
  ctx.set_font_size(font_size) 

  for line in lines:
    ctx.move_to(x, y)
    ctx.show_text(line)
    y = y + line_spacing + font_size

def WriteEnvelope(surface, lines):
  ctx = cairo.Context(surface)
  ctx.select_font_face('Sans')
  ctx.set_source_rgb(0,0,0)

  ctx.move_to(140, 180)
  _WriteLines(ctx, lines, 14, 4)



      

  

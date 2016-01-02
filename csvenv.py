import cairo

def _WriteLines(ctx, lines, font_size, line_spacing=2):

  x, y = ctx.get_current_point()
  
  ctx.set_font_size(font_size) 

  for line in lines:
    ctx.move_to(x, y)
    ctx.show_text(line)
    y = y + line_spacing + font_size

def _WriteEnvelope(ctx, to_address, from_address):
  ctx.select_font_face('Sans')
  ctx.set_source_rgb(0,0,0)

  ctx.move_to(40, 40)
  _WriteLines(ctx, from_address.splitlines(), 11)

  ctx.move_to(160, 120)
  _WriteLines(ctx, to_address.splitlines(), 14, 4)

  
def WriteEnvelopes(surface, to_addresses, from_address):
  ctx = cairo.Context(surface)
  for to_address in to_addresses:
    _WriteEnvelope(ctx, to_address, from_address)

    surface.show_page()







      

  

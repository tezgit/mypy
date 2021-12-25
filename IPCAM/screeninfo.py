from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")

window = Gtk.Window()
screen = window.get_screen()
ww = screen.get_width()
hh = screen.get_height()
print("width = {} ::: height = {}" .format(ww, hh))

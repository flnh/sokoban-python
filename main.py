import curses
import MapReader
import Player
import Box

def main(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)

    mapReader = MapReader.MapReader('map')

    if mapReader.verifyMap() == False:
        curses.endwin()
        exit()

    player = Player.Player()
    box = Box.Box()

    mapReader.displayMap(stdscr)
    while True:
        
        entry = stdscr.getch()
        globals()['entry'] = entry
        stdscr.clear()
        
        if entry == 27 or entry == 113:
            curses.endwin()
            exit()
            
        if entry == curses.KEY_UP:
            player.moveUp()
            mapReader.displayMap(stdscr)
            stdscr.refresh()

        if entry == curses.KEY_DOWN:
            player.moveDown()
            mapReader.displayMap(stdscr)
            stdscr.refresh()

        if entry == curses.KEY_LEFT:
            player.moveLeft()
            mapReader.displayMap(stdscr)
            stdscr.refresh()

        if entry == curses.KEY_RIGHT:
            player.moveRight()
            mapReader.displayMap(stdscr)
            stdscr.refresh()
        
if __name__ == "__main__":
    curses.wrapper(main)
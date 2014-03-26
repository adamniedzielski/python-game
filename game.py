
import wx

class Game(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.__init_configuration()
        self.__InitUI__()

    def __init_configuration(self):
      self.configuration = [
        [1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1]
      ]

    def __InitUI__(self):
      self.panel = wx.Panel(self)
      sizer = wx.GridSizer(5, 5)
      self.board = [None] * 25

      for i in range(25):
        row, column = self._in_two_dimensions(i)
        if self.configuration[row][column] == 1:
          button = wx.Button(self.panel)
          button.SetBackgroundColour('yellow')
          self.board[i] = button
          button.Bind(wx.EVT_BUTTON, lambda event, i = i: self._on_click(event, i))
          sizer.Add(button, 0, wx.EXPAND)
        else:
          sizer.Add((0, 0), 0, wx.EXPAND)

      self.panel.SetSizer(sizer)
      sizer.Fit(self)

      self.SetTitle('Game')
      self.SetSize((600, 600))
      self.Centre()
      self.Show(True)

    def _on_click(self, event, i):
      self._toggle_color(self.board[i])
      neighbours = self._neighbours(self._in_two_dimensions(i))

      for neighbour in neighbours:
        element = self.board[self._in_one_dimension(neighbour)]
        if element:
          self._toggle_color(element)

      self.__end_if_win()
      

    def _toggle_color(self, button):
      if button.GetBackgroundColour() == "yellow":
        button.SetBackgroundColour("red")
      else:
        button.SetBackgroundColour("yellow")

    def _in_two_dimensions(self, i):
      return (i / 5, i % 5)

    def _in_one_dimension(self, coordinates):
      return coordinates[0] * 5 + coordinates[1]

    def _neighbours(self, coordinates):
      result = []

      if coordinates[0] > 0:
        result.append((coordinates[0] - 1, coordinates[1]))

      if coordinates[1] > 0:
        result.append((coordinates[0], coordinates[1] - 1))

      if coordinates[0] < 4:
        result.append((coordinates[0] + 1, coordinates[1]))

      if coordinates[1] < 4:
        result.append((coordinates[0], coordinates[1] + 1))

      return result

    def __end_if_win(self):
      if self.__win():
        dialog = wx.MessageDialog(None, 'You win!', 'Info', wx.OK)
        dialog.ShowModal()
        self.Close()

    def __win(self):
      for element in self.board:
        if element and element.GetBackgroundColour() == "yellow":
          return False

      return True


   
app = wx.App()
Game(None)
app.MainLoop()

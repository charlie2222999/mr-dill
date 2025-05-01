colors = {
    'white':'ban',
    'red':'dearg',
    'green': 'glas',
    'blue': 'gorm',
    'black': 'dubh',
}
color = input('enter a color:')
translation = colors(color)
color = input('enter a color:')
translation = colors.get(color)
color = input('enter a color:')
translation = colors.pop(color)

    
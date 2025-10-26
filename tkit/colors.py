txt-style = {
    color: {
        black: "\033[30m",
        red: "\033[31m",
        green: "\033[32m",
        yellow: "\033[33m",
        blue: "\033[34m",
        magenta: "\033[35m",
        cyan: "\033[36m",
        white: "\033[37m",
        
        # Colores Brillantes (ANSI Bright Colors)
        light-black: "\033[90m", # Gray o Bright Black
        light-red: "\033[91m",
        light-green: "\033[92m",
        light-yellow: "\033[93m",
        light-blue: "\033[94m",
        light-magenta: "\033[95m",
        light-cyan: "\033[96m",
        light-white: "\033[97m" # Bright White
    },

    background: {
        black: "\033[40m",
        red: "\033[41m",
        green: "\033[42m",
        yellow: "\033[43m",
        blue: "\033[44m",
        magenta: "\033[45m",
        cyan: "\033[46m",
        white: "\033[47m",
        
        # Fondos Brillantes (ANSI Bright Backgrounds)
        light-black: "\033[100m", 
        light-red: "\033[101m",
        light-green: "\033[102m",
        light-yellow: "\033[103m",
        light-blue: "\033[104m",
        light-magenta: "\033[105m",
        light-cyan: "\033[106m",
        light-white: "\033[107m"
    },

    style: {
        bold: "\033[1m",
        dim: "\033[2m", # Baja intensidad o tenue
        italic: "\033[3m", 
        underline: "\033[4m",
        blink: "\033[5m", # Parpadeo lento
        reverse: "\033[7m", # Invierte foreground y background
        hidden: "\033[8m", # Oculto (invisible)
        strikethrough: "\033[9m" # Tachado
    },
    
    # Reset para terminar todos los estilos
    reset: "\033[0m"
}

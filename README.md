# TKit
> Created by VoidMask (v0idm4sk)   
TKit is an all-in-one Python library for the CLI, with functions like text color, decorated inputs, loading functions, argument functions, and more. Try TKit and enjoy the ease of programming for CLI in Python

## Installation (↓)
<p style="opacity: 0.7">Package in development...</p>

## Use </>
Print With color:
```main.py
import tkit

tkit.printer("Hello World With TKit!", color="blue")
```

Inputs decorated:
```main.py
import tkit

codeIn = tkit.in("Yes or No >> ", color="white", bold-txt=True)

if codeIn.argv[0].lower() == ("yes", "y"):
    tkit.printer("Your value is correct")
else:
    tkit.printer("Your value is incorrect")
```

Loaders in CLI:
```main.py
import tkit

print("Downloading...")
tkit.loader("/", time="30s") # / - \ |
```

For more information, visit https://tkit.pythonanywhere.com/code-help

## License (C)
This Python library is licensed under the MIT license. Which says that the source code can be edited, merged, copied, and distributed, and requires that the copyright notice and license text be maintained on all copies or substantial parts of the software.
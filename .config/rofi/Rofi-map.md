# Basic structure
```
|------------------------------------------------------------------------------------|
| window {BOX:vertical}                                                              |
| |-------------------------------------------------------------------------------|  |
| | mainbox  {BOX:vertical}                                                       |  |
| | |---------------------------------------------------------------------------| |  |
| | | inputbar {BOX:horizontal}                                                 | |  |
| | | |---------| |-----------------------------------------------------| |---| | |  |
| | | | prompt  | | entry                                               | |ci | | |  |
| | | |---------| |-----------------------------------------------------| |---| | |  |
| | |---------------------------------------------------------------------------| |  |
| |                                                                               |  |
| | |---------------------------------------------------------------------------| |  |
| | | message                                                                   | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | | | textbox                                                               | | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | |---------------------------------------------------------------------------| |  |
| |                                                                               |  |
| | |---------------------------------------------------------------------------| |  |
| | | listview                                                                  | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | | | element                                                               | | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | | | element                                                               | | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | | | element                                                               | | |  |
| | | |-----------------------------------------------------------------------| | |  |
| | |---------------------------------------------------------------------------| |  |
| |                                                                               |  |
| | |---------------------------------------------------------------------------| |  |
| | |  mode-switcher {BOX:horizontal}                                           | |  |
| | | |---------------|   |---------------|  |--------------| |---------------| | |  |
| | | | Button        |   | Button        |  | Button       | | Button        | | |  |
| | | |---------------|   |---------------|  |--------------| |---------------| | |  |
| | |---------------------------------------------------------------------------| |  |
| |-------------------------------------------------------------------------------|  |
|------------------------------------------------------------------------------------|
```

# Error message structure
```
|-----------------------------------------------------------------------------------|
| window {BOX:vertical}                                                             |
| |------------------------------------------------------------------------------|  |
| | error-message {BOX:vertical}                                                 |  |
| | |-------------------------------------------------------------------------|  |  |
| | | textbox                                                                 |  |  |
| | |-------------------------------------------------------------------------|  |  |
| |------------------------------------------------------------------------------|  |
|-----------------------------------------------------------------------------------|
```

# Theme file structure
```
* {}
window {}
    mainbox {}
        inputbar {}
            prompt {}
            entry {}
            case-indicator {}
        message {}
            textbox {}
        listview {}
            element {}
            element selected {}
            element alternate {}
        mode-switcher {}
            Button {}



        error-message {}
            textbox {}
```
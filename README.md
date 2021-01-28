# televlc


```go
                                                      ######                 
                                                ##################           
             ###                                ##    #############          
            #####                               ###################          
           #######                                       ##########          
          ********                     ############################  ****** 
         ***********                  ############################# *********
        ##*********##                ##############################  *********
       ###############   <-------->  ############                 *************
      *##############*                #########   *****************************
     *******************               ######### *****************************
     *******************                ######## ***************************  
 ####******************####                     *********                    
########***********#########                    *******************          
############################                    *************    **          
############################                     *****************
                                                      *******
```

Python library to control [VLC media player](https://www.videolan.org/vlc/index.es.html) via telnet protocol


## Installation

```
pip install televlc
```

## Usage

    import televlc

    # Initialize the vlc object
    vlc = televlc.VLC()

    # Open a VLC instance and create the telnet interface
    vlc.start_telnet_interface()

    # Connect to the telnet interface
    vlc.connect_to_telnet_interface()

    # Run a command (volume up)
    vlc.do(["volup", "50"])

    # Disconnect from telnet interfac
    vlc.disconnect_from_telnet_interface()
    # or
    vlc.do(["exit"])
    # or end VLC instance and telnet interface
    vlc.do(["shutdown"])

## Supported commands

### VLM commands

> **_NOTE:_**  There is no support for VLM commands... yet

### CLI commands

| command | description | support |
| --- | --- | --- |
| add XYZ | add XYZ to playlist | |
| enqueue XYZ | queue XYZ to playlist | |
| playlist | show items currently in playlist | |
| search [string] | search for items in playlist (or reset search) | |
| delete [X] | delete item X in playlist | |
| move [X][Y] | move item X in playlist after Y | |
| sort key | sort the playlist | |
| sd [sd] | show services discovery or toggle | |
| play | play stream | |
| stop | stop stream | |
| next | next playlist item | |
| prev | previous playlist item | |
| goto, gotoitem | goto item at index | |
| repeat [on off] | toggle playlist repeat | |
| loop [on off] | toggle playlist loop | |
| random [on off] | toggle playlist random | |
| clear | clear the playlist | |
| status | current playlist status | |
| title [X] | set/get title in current item | |
| title_n | next title in current item | |
| title_p | previous title in current item | |
| chapter [X] | set/get chapter in current item | |
| chapter_n | next chapter in current item | |
| chapter_p | previous chapter in current item | |
| seek X | seek in seconds, for instance `seek 12' | |
| pause | toggle pause | |
| fastforward | set to maximum rate | |
| rewind | set to minimum rate | |
| faster | faster playing of stream | |
| slower | slower playing of stream | |
| normal | normal playing of stream | |
| rate [playback_rate] | set playback rate to value | |
| frame | play frame by frame | |
| fullscreen, f, F [on off] | toggle fullscreen | |
| info [X] | information about the current stream (or specified id) | |
| stats | show statistical information | |
| get_time | seconds elapsed since stream's beginning | |
| is_playing | 1 if a stream plays, 0 otherwise | |
| get_title  | the title of the current stream | |
| get_length | the length of the current stream | |
| volume [X] | set/get audio volume | |
| volup [X]  | raise audio volume X steps | |
| voldown [X] | lower audio volume X steps | |
| achan [X] | set/get stereo audio output mode | |
| atrack [X] | set/get audio track | |
| vtrack [X] | set/get video track | |
| vratio [X] | set/get video aspect ratio | |
| vcrop, crop [X] | set/get video crop | |
| vzoom, zoom [X] | set/get video zoom | |
| vdeinterlace [X] | set/get video deinterlace | |
| vdeinterlace_mode [X] | set/get video deinterlace mode | |
| snapshot | take video snapshot | |
| strack [X] | set/get subtitle track | |
| vlm | load the VLM | |
| description | describe this module | |
| help, ? [pattern] | a help message | |
| longhelp [pattern] | a longer help message | |
| lock | lock the telnet prompt | |
| logout | exit (if in a socket connection) | |
| quit | quit VLC (or logout if in a socket connection) | |
| shutdown | shutdown VLC | |



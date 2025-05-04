# gitk on MacOS

`gitk` is a great way to visualize a git history. The main advantage over
other, often better-looking alternatives is that is shows more history.

It is in homebrew as `git-gui`.

Whenever `gitk` gets updated on my Mac, I get the following error:

    % gitk
    2024-05-09 14:00:42.828 wish[3274:109555] ApplePersistence=NO
    Error in startup script: 2024-05-09 14:00:42.904 osascript[3282:109574] ApplePersistence=NO
        while executing
    "exec osascript -e [format {
            tell application "System Events"
                set frontmost of processes whose unix id is %d to true
            end te..."
        invoked from within
    "if {[tk windowingsystem] eq "aqua"} {
        exec osascript -e [format {
            tell application "System Events"
                set frontmost of processes ..."
        (file "/opt/homebrew/bin/gitk" line 12321)

A [Solution](https://stackoverflow.com/questions/56828880/running-gitk-leads-to-cryptic-error-message-on-macos-mojave) is to remove the following lines:

    # on OSX bring the current Wish process window to front
    if {[tk windowingsystem] eq "aqua"} {
        exec osascript -e [format {
            tell application "System Events"
                set frontmost of processes whose unix id is %d to true
            end tell
        } [pid] ]
    }

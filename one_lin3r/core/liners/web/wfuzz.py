class info:
    author      = "snix0"
    description = "Fuzz hidden directories with wfuzz"
    function    = "Web"
    liner       = "wfuzz --hc 404 -w /usr/share/wordlists/dirb/common.txt -u 'http://TARGET/FUZZ.txt' -f wfuzz.html,htm"

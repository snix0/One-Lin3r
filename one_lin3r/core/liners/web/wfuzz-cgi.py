class info:
    author      = "snix0"
    description = "Fuzz CGI with wfuzz"
    function    = "Web"
    liner       = "wfuzz --hc 404 -w /usr/share/wordlists/dirb/vulns/cgis.txt -u 'http://TARGET/FUZZ' -f wfuzz.cgi.html,htm"

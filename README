PHP heredoc gettext extractor
=============================

Copyright (C) 2012 Dafydd Crosby

This script can be used to extract gettext strings from inside heredoc 
strings in PHP. It was written as it appears this use case will in all
likelihood not be addressed by the gettext team (understandably). Quite
frankly, had I known this at the outset, I probably would not have done 
it in the first place ;-)

Usage
-----

Run `extract.py [files]`, and it should output to "hd_messages.po".
After that, use msgcat to combine "hd_messages.po" with whatever .po file you're
currently using. Then use your regular gettext conversion flow.

TODO
----

Write some tests that check for broken gettext blocks
Ensure we're getting heredoc strings from inside PHP blocks
Make 'search_heredoc_string' less ugly
Ensure we're escaping strings like the gettext people
Add commented out line numbers (nice to have, not critical)
Use getopts...?

FAQ
---

Q. Why was this written in Python and not PHP?
A. Because deadlines called for it :-)

License
-------

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.

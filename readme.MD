<h3>Before running</h3>
make sure to have the <i> latest version of Python</i> installed on your system and the Python executable is in your
PATH variable.

<hr>

<h6>Program dependencies</h6>
<ul>
    <li>Paramiko</li>
    <li>Scp</li>
</ul>

<h6>Installing dependencies</h6>
<p>If you know how to work with pipenv all you need to do is
<code>pipenv install</code> and it'll install the required dependencies</p>
<p>If you don't know how to work with pipenv, then do the following to globally install dependencies</p>
<ul>
    <li><code>pip install paramiko</code></li>
    <li><code>pip install scp</code></li>
</ul>

<hr>

<h6>Running the script</h6>
<p>After all dependencies have been installed,
use the following to run the script from the directory
<code>main.py</code> is located in.</p>
<ul><li><code>python main.py [options]</code></li></ul>
<p>List of options:</p>
<ul>
    <li>host</li>
    <ul><li>Sets the remote host for the program</li></ul>
    <li>-u / --upload</li>
    <ul><li>Sets the program to upload files/directories</li></ul>
    <li>-d / --download</li>
    <ul><li>Sets the program to download files/directories</li></ul>
    <li>-un / --username</li>
    <ul><li>Sets the username for use to connect to remote host</li></ul>
    <li>-lp / --local-path</li>
    <ul><li>Sets the local path to download to/upload from</li></ul>
    <li>-rp / --remote-path</li>
    <ul><li>Sets the remote path to download to/upload from</li></ul>
    <li>-r / --recursive</li>
    <ul><li>Sets the program to download/upload recursively. Allows for directory uploads/downloads</li></ul>
</ul>

<hr>
<h1>DISCLAIMER</h1>

<ul>
    <li>
        <h5>Password is never kept after exiting the program. It's only available while the program is running</h5>
    </li>
</ul>


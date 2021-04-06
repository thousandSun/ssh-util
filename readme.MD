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
<i>pipenv install</i> and it'll install the required dependencies</p>
<p>If you don't know how to work with pipenv, then do the following to globally install dependencies</p>
<ul>
    <li>pip install paramiko</li>
    <li>pip install scp</li>
</ul>

<hr>

<h6>Running the script</h6>
<p>After all dependencies have been installed,
use the following to run the script from the directory
<i>main.py</i> is located in.</p>
<ul><li>python main.py [options]</li></ul>
<p>List of options:</p>
<ol>
    <li>--upload / --download
        <ul><li>Tells the script whether to upload or download file/directory</li></ul>
    </li>
    <li>--username "username"
        <ul><li>username to log into remote server</li></ul>
    </li>
    <li>[hostAddress]
        <ul><li>IP address of remote host</li></ul>
    </li>
    <li>[localpath] / [remotepath]
        <ul>
            <li>If first option was "--upload" then this option holds path to local file for upload</li>
            <li>If first option was "--download" then this option holds path to remote file for download</li>
        </ul>
    </li>
    <li>[remotepath] / [localpath]
        <ul>
            <li>If first option was "--upload" then this option holds remote path to where you want to upload the file to</li>
            <li>If first option was "--download" then this option holds local path to where on your local machine you want the file downloaded</li>
        </ul>
    </li>
    <li>--recursive / -r
        <ul>
            <li>Optional</li>
            <li>Allows to recursively upload/download directories</li>
        </ul>
    </li>
</ol>

<hr>
<h1>DISCLAIMER</h1>

<ul>
    <li>
        <h5>As of now, the syntax to run the script is static. Meaning that you have to conform to the order of the options.
        I'll be trying to figure out how to make the options dynamic.</h5>
    </li>
    <li>
        <h5>Password is never kept after exiting the program. It's only available while the program is running</h5>
    </li>
</ul>


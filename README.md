# Visual Studio Code Snippet
Code snippet for visual studio code

More details about visual studui code snippet : https://code.visualstudio.com/docs/editor/userdefinedsnippets

## How to add code snippet

<ol>
  <li> Select File &rarr; Preferences &rarr; User Snippets
  </li>
  <li> Type programming language that you wnat to create the code snippet for <br/>
        <img src="https://github.com/Pajri/Visual-Studio-Code-Snippet/blob/master/Java/assets/java%20code%20snippet.gif"/> <br/>
        This is example of the code snippet. I write this code snippet for java.
<pre>
"Print to console": {
    "prefix": "sout",
    "body": [
        "System.out.println(\"${1}\");"
    ],
    "description": "Generate System.out.println"
}
</pre>
    Explanation for the code snippet : <br/>
    <table>
      <tr>
        <td><strong>Print to console</strong></td><td>Name of code snippet</td>
      </tr>
      <tr>
        <td><strong>Prefix</strong></td><td>Text that will trigger code completition</td>
      </tr>
      <tr>
        <td><strong>Body</strong></td><td>The code. ${1} is to place cursor after code completition</td>
      </tr>
      <tr>
        <td><strong>Description</strong></td><td>Description of the code snippet</td>
      </tr>
    </table>
    
  </li>
  <li> Result : <br/>
    <img src="https://github.com/Pajri/Visual-Studio-Code-Snippet/blob/master/Java/assets/code%20snippet%20result.gif?"/>
  </li>
</ol>

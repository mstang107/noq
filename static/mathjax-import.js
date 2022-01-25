var script = document.createElement('script'); 
script.src = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js"; 
document.head.appendChild(script);

MathJax.Hub.Config({
	jax: ["input/TeX", "output/HTML-CSS"],
	extensions: ["tex2jax.js"],
	"HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"] },
	tex2jax: { inlineMath: [ ["$", "$"], ["\\(","\\)"] ], displayMath: [ ["$$","$$"], ["\\[", "\\]"] ], processEscapes: true, ignoreClass: "tex2jax_ignore|dno" },
	TeX: { noUndefined: { attributes: { mathcolor: "red", mathbackground: "#FFEEEE", mathsize: "90%" } } },
	messageStyle: "none"
});
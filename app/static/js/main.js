$(function(){
	"use strict";

	// Editor functionality
	if($("textarea[name='markdown']").length > 0) {

		var EditorTextArea = $("textarea[name='markdown']")[0];
		var addnewline = function(cm, text, startOnNewLine, pos){
			var startOnNewLine = (startOnNewLine) ? "\n" : "";
			var doc = cm.getDoc();
			var cursor = doc.getCursor(); // gets the line number in the cursor position
			var line = doc.getLine(cursor.line); // get the line contents
			var position = (pos) ? pos : { // create a new object to avoid mutation of the original selection
				line: cursor.line,
				ch: line.length // set the character position to the end of the line
			}
			doc.replaceRange(startOnNewLine+text+"\n", position); // adds a new line
		}
		var makeSureHeadingIsAdded = function(markdown, cm) {
			var heading = markdown.split(/\n/)[0];
			// If no heading let add it...
			if( heading.substring(0, 2) != "# ") {
				addnewline(cm, "# Subject/Title *required*", false, { line:0, ch:0 });
			}
		}
		var preperehtml = function(plainText, cb) {
			// Use internal renderer but make some changes...
			var html = simplemde.markdown(plainText);
			var content = $('<div></div>').append(html);

			// Make sure we remove ribbon image from preview 
			// and final html
			var ribbon = content.find("img[alt='ribbon']").first();
			if(ribbon.length) {
				var ribbonImage = ribbon.attr('src');
				$(".ribbon.editor").css('background-image', 'url(' +ribbonImage+ ')');
				$("input[name='ribbon'").val(ribbonImage);
				ribbon.parent().remove();
			} else {
				$(".ribbon.editor").css('background-image', 'none');
			}

			// Let execute any callback if we have...
			if(cb && typeof cb == "function"){ return cb(content); }
			// Return fromated html
			return content.html();
		}
		// Clean the content before saving...
		var beforeSave = function() {
			var compiledHtml = preperehtml(simplemde.value(), function(content) {
				// Make sure we remove title from final html
				var title = content.find("h1").first();
				$("input[name='title'").val(title.text());
				title.remove();
				// Return fromated html
				return content.html();
			});
			// Set the content for the post
			$("input[name='content'").val(compiledHtml);
		}
		// Save the post...
		$("#submit").click(function(e){ 
			//e.preventDefault(); 
			beforeSave(); 
		});
		// Init the simple mde
		var simplemde = new SimpleMDE({ 
			element: EditorTextArea, 
			spellChecker: false,
			placeholder: "***You must use at least one h1 heading \n"+ 
			"# Subject/Title *required* \n\n"+ 
			"***Set this to add background to your post \n"+
			"![ribbon](https://s.yimg.com/uy/build/images/sohp/hero/lax-den3.jpg)\n\n"+
			"***Here write your awsome post \n"+
			"## Content *required*",
			previewRender: function(plainText) {
				return preperehtml(plainText);
			},
			toolbar: [
				"undo", "redo",
				"bold", "italic", "strikethrough", "heading-2", 
				"heading-3",
				"|",
				"quote", "unordered-list", "ordered-list",
				"|",
				"link", "image", 
				"|",
				"preview", "side-by-side", "fullscreen",
				"|",
				{
					name: "custom",
					action: function (editor){
						addnewline(editor.codemirror, 
							"![ribbon](https://s.yimg.com/uy/build/images/sohp/hero/lax-den3.jpg)", 
								true);
					},
					className: "fa fa-map",
					title: "Add Ribbon background",
				},
				"|",
			]
		});
		// Keep track and if no heading add it..
		simplemde.codemirror.on("focus", function(){
			makeSureHeadingIsAdded(simplemde.value(), simplemde.codemirror);
		});
		simplemde.codemirror.on("blur", function(){
			makeSureHeadingIsAdded(simplemde.value(), simplemde.codemirror);
		});

	}

});

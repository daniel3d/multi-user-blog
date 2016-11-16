'use strict';

// Load libraries...
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    open = require('gulp-open'),
    gutil = require('gulp-util'),
    spawn = require('child_process').spawn,
    livereload = require('gulp-livereload');

// Copy vendor libs...
gulp.task('vendor', function() {
/*	gulp.src([
		'node_modules/codemirror/lib/codemirror.css',
		'node_modules/codemirror/lib/codemirror.js',
		'node_modules/codemirror/mode/markdown/markdown.js',
		'node_modules/codemirror/theme/base16-light.css',
		'node_modules/markdown-it/dist/markdown-it.min.js',
		'node_modules/markdown-it-footnote/dist/markdown-it-footnote.js'
	]).pipe(gulp.dest('app/static/vendor'));
*/});

// Compile sass to css...
gulp.task('sass', function() {
	gulp.src('app/static/scss/**/*.scss')
		.pipe(sass({includePaths: ['app/static/scss']}))
		.pipe(gulp.dest('app/static/css/compiled'))
		.pipe(livereload());
});

// Watch for changes and run the live reload...
gulp.task('watch', function() {
	livereload.listen(35729);
	gulp.watch('app/static/scss/**/*.scss', ['sass']);
	gulp.watch('app/static/js/**/*.js', livereload.reload);
	gulp.watch('app/views/**/*.html', livereload.reload);
	gulp.watch('app/*.py', livereload.reload);
});

// Start google sdk dev server...
gulp.task('server', function(cb){
	var server = spawn('cmd.exe', 
		['/s', '/c', 'dev_appserver.py --port=9999 app.yaml'])
	
	server.stderr.on('data', function (data) {
		gutil.log(gutil.colors
			.yellow(data.toString().trim()));
	});
	server.stdout.on('data', function (data) {
		console.log(data);
		gutil.log(gutil.colors
			.yellow(data.toString()));
	});
	server.on('close', function(code) {
		gutil.beep();
		gutil.log(gutil.colors
			.yellow("server closed with exit code [", code, "]"));
	});
	server.on('error', function( err ){ 
		gutil.beep();
		gutil.log(gutil.colors
			.red("server error: [", err.toString().trim(), "]")); 
	});

	gulp.src(__filename)
		.pipe(open({uri: 'http://localhost:8000/instances'}))
		.pipe(open({uri: 'http://localhost:9999'}));

});

// Run the tasks...
gulp.task('default', ['vendor', 'server', 'sass', 'watch']);
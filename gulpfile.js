'use strict';

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    livereload = require('gulp-livereload')

gulp.task('sass', function() {
  return gulp.src('app/static/scss/**/*.scss')
      .pipe(sass({includePaths: ['app/static/scss']}))
      .pipe(gulp.dest('app/static/css/compiled'))
      .pipe(livereload());
})

gulp.task('watch', function() {
  livereload.listen(35729);
  gulp.watch('app/static/scss/**/*.scss', ['sass']);
})


gulp.task('default', ['watch']);
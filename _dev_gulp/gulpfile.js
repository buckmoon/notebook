var gulp = require('gulp');
var sass = require('gulp-sass');
var sassGlob = require("gulp-sass-glob");
var watch = require('gulp-watch');
var autoprefixer = require('gulp-autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
var filter = require('gulp-filter');
var plumber = require('gulp-plumber');

var path = {
  'inputFile': ['../notebook/static/notebook/miw_custom_theme/override.sass']
};

gulp.task('default', ['sass', 'watch']);

gulp.task('sass', function() {
  return gulp
  .src(path.inputFile)
  .pipe(plumber())
  .pipe(sourcemaps.init())
  .pipe(sassGlob())
  .pipe(sass({
    compress: true
  }))
  .pipe(autoprefixer({
    browsers: ['last 2 versions'],
    cascade: false
  }))
  //.pipe(filter('**/*.css'))
  .pipe(sourcemaps.write('./'))
  .pipe(gulp.dest("../notebook/static/notebook/css"));
});

gulp.task('watch', function(){
  watch("../notebook/static/notebook/miw_custom_theme/**/*.sass", function () {
    gulp.start(['sass']);
  });
});

var gulp = require('gulp');

/* plugins:
** npm install --save-dev 
** gulp-uglify gulp-rename gulp-concat gulp-sass 
** gulp-minify-css gulp-autoprefixer 
*/
const uglify     = require('gulp-uglify'), // js compress
      rename     = require('gulp-rename'), // file rename
      concat     = require('gulp-concat'), // file combine
      sass       = require('gulp-sass'),
      cleanCSS   = require('gulp-clean-css'),
      autoprefix = require('gulp-autoprefixer');

//  var minifycss  = require('gulp-minify-css'),

/* path
** source, build 
*/
const src = {
  js: 'assets/src/js/*.js',
  sass: 'assets/src/sass/main.scss',
  sassdir: 'assets/src/sass/*.scss',
  mainjs: [
      'assets/src/js/anchor.js', 
      'assets/src/js/uptotop.js', 
      'assets/src/js/jquery-ui-widget.js', 
      'assets/src/js/jquery.tocify.js', 
      'assets/src/js/app.js'
  ]
};
const dist = {
  js: 'assets/dist/js/',
  css: 'assets/dist/css/'
};

/* minifyjs
** https://github.com/gruntjs/grunt-contrib-uglify#preservecomments
** {preserveComments : 'some'} reserve lisence 
*/
gulp.task('minifyjs', function () {
  gulp.src(src.js)
    .pipe(rename({suffix: '.min'}))
    .pipe(uglify({preserveComments : 'some'}))
    .pipe(gulp.dest(dist.js));
});

/* combinejs: 
** minify js 
*/
gulp.task('combinejs', function () {
  gulp.src(src.mainjs)
    .pipe(uglify({preserveComments : 'some'}))
    .pipe(concat('main.min.js'))
    .pipe(gulp.dest(dist.js));
});

/* sass: 
** compile sass
*/
gulp.task('sass', function() {
    gulp.src(src.sass)
      .pipe(sass().on('error', sass.logError))
      .pipe(autoprefix())
      //.pipe(minifycss())
      .pipe(rename({suffix: '.min'}))
      .pipe(cleanCSS())
      .pipe(gulp.dest(dist.css));
});

/* default */
gulp.task('default', function(){
    gulp.start(['combinejs','sass']);
});

/* watch: 
** excute task when less file is changed 
*/
gulp.task('watch', function() {
  gulp.watch(src.js, ['minifyjs','combinejs']);
  gulp.watch(src.sassdir, ['sass']);
});

gulp.task('watchcss', function() {
  gulp.watch(src.sassdir, ['sass']);
});
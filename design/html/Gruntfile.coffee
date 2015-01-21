module.exports = (grunt) ->
  grunt.initConfig
    pkg: grunt.file.readJSON "package.json"
    compass:
      app:
        options:
          config: "config.rb"
    watch:
      styles:
        files: [
          "config.rb"
          "static/sass/**"
        ]
        tasks: "default"
      templates:
        files: ["templates/**"]
        options: {livereload: true}
      css:
        files: "static/css/*.css"
        options: {livereload: true}
  grunt.loadNpmTasks "grunt-contrib-compass"
  grunt.loadNpmTasks "grunt-contrib-watch"
  grunt.registerTask "default", ["compass"]

// build main.min.js
// spawned by gulp to allow parallelism

var rjs = require('requirejs').optimize;

var name = process.argv[2];

var rjs_config = {
  name: name + '/js/main',
  out: './notebook/static/' + name + '/js/main.min.js',
  baseUrl: 'notebook/static',
  preserveLicenseComments: false, // license comments conflict with sourcemap generation
  generateSourceMaps: true,
  optimize: "none",
  paths: {
    underscore : 'components/underscore/underscore-min',
    backbone : 'components/backbone/backbone-min',
    jed: 'components/jed/jed',
    jquery: 'components/jquery/jquery.min',
    json: 'components/requirejs-plugins/src/json',
    text: 'components/requirejs-text/text',
    bootstrap: 'components/bootstrap/js/bootstrap.min',
    bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
    "jquery-ui": 'components/jquery-ui/jquery-ui.min',
    moment: 'components/moment/min/moment-with-locales',
    codemirror: 'components/codemirror',
    xterm: 'components/xterm.js/index',
    'xtermjs-fit': 'components/xterm.js-fit/index',
    typeahead: 'components/jquery-typeahead/dist/jquery.typeahead',
    contents: 'empty:',
    custom: 'empty:',
  },
  map: { // for backward compatibility
    "*": {
        "jqueryui": "jquery-ui",
    }
  },
  shim: {
    typeahead: {
            deps: ["jquery"],
            exports: "typeahead"
          },
    underscore: {
      exports: '_'
    },
    backbone: {
      deps: ["underscore", "jquery"],
      exports: "Backbone"
    },
    bootstrap: {
      deps: ["jquery"],
      exports: "bootstrap"
    },
    bootstraptour: {
      deps: ["bootstrap"],
      exports: "Tour"
    },
    "jquery-ui": {
      deps: ["jquery"],
      exports: "$"
    },
  },

  exclude: [
    "custom/custom",
  ]
};

rjs(rjs_config, console.log, function (err) {
  console.log("Failed to build", name, err);
  process.exit(1);
});
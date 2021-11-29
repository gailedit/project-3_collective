/* Initialize Quill editor */
var quill = new Quill('#editor', {
  theme: 'snow'
});

var options = {
  debug: 'info',
  modules: {
    toolbar: '#toolbar'
  },
  placeholder: 'Compose an epic...',
  readOnly: true,
  theme: 'snow'
};
var editor = new Quill('#editor', options);
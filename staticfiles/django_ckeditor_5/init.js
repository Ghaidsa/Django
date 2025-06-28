document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.django_ckeditor_5').forEach((el) => {
    ClassicEditor
      .create(el)
      .catch(error => {
        console.error('CKEditor error:', error);
      });
  });
});

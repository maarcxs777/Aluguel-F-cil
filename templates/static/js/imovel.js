function previewImages(event) {
    const previewContainer = document.getElementById('upload-preview');
    previewContainer.innerHTML = ''; 

    const files = event.target.files;
    Array.from(files).forEach(file => {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            previewContainer.appendChild(img);
        };
        reader.readAsDataURL(file);
    });
}

document.getElementById('anuncio-form').addEventListener('submit', function(e) {
    e.preventDefault();
    Swal.fire({
        title: 'Enviando...',
        text: 'Seu anúncio está sendo processado.',
        icon: 'info',
        showConfirmButton: false,
        allowOutsideClick: false
    });

    // Simulação de envio
    setTimeout(function() {
        Swal.fire({
            title: 'Anúncio enviado com sucesso!',
            icon: 'success',
            confirmButtonText: 'OK'
        });
        document.getElementById('anuncio-form').reset();
        document.getElementById('upload-preview').innerHTML = ''; // Limpa a pré-visualização
    }, 2000); // Simula o tempo de processamento
});
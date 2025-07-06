document.getElementById('promptForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const prompt = document.getElementById('prompt').value;
    const loading = document.getElementById('loading');
    const video = document.getElementById('resultVideo');
    loading.style.display = 'block';
    video.style.display = 'none';
    video.src = '';
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: new URLSearchParams({prompt}),
        });
        const data = await response.json();
        if (data.video_url) {
            video.src = data.video_url + '?t=' + Date.now(); // prevent caching
            video.style.display = 'block';
        } else {
            alert('Error: ' + (data.error || 'Unknown error'));
        }
    } catch (err) {
        alert('Failed to generate video.');
    }
    loading.style.display = 'none';
}); 
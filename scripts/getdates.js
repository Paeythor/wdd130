<script>
  const currentYear = new Date().getFullYear();
  document.getElementById('currentyear').textContent = currentYear;

  const lastModifiedDate = document.lastModified;
  document.getElementById('lastModified').textContent = `Last Modified: ${lastModifiedDate}`;

  const imageFolder = "";
  const images = [
    "images/utahlandscapes/arches-utah-fact.jpg",
    "images/utahlandscapes/lake.jpeg",
    "images/utahlandscapes/trees.jpeg",
    "images/utahlandscapes/utahriver.jpeg",
    "images/utahlandscapes/waterfall.jpeg",
    "images/utahlandscapes/snowmount.jpeg"
  ];
  let currentIndex = 0;
  const imgElement = document.getElementById("slideshow");

  function changeImage() 
  {
    currentIndex = (currentIndex + 1) % images.length;
    imgElement.src = images[currentIndex];
  }

  setInterval(changeImage, 3000);
</script>

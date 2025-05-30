import { Slideshow } from './slideshow.js';

const basePath = "/static/images/";
const films = ["lore_koehm", "heimatfilm", "elfriede_bergmeir", "heinz_eiting", "adolf_zeeb"];
const numImages = 5;

async function checkFileExistence(film, index) {
    const filePathPng = `${basePath}${film}/img${String(index + 1).padStart(2, '0')}.png`;
    const filePathJpg = `${basePath}${film}/img${String(index + 1).padStart(2, '0')}.jpg`;

    const fileExists = async (url) => {
        const res = await fetch(url, { method: 'HEAD' });
        return res.ok;  // Returns true if the file exists
    };

    if (await fileExists(filePathPng)) {
        return filePathPng;
    } else if (await fileExists(filePathJpg)) {
        return filePathJpg;
    }
    return null;  // Return null if neither file exists
}

async function loadImages() {
    const imageSources = await Promise.all(films.map(async (film) => {
        const sources = await Promise.all(Array.from({ length: numImages }, async (_, i) => {
            return checkFileExistence(film, i);
        }));
        return sources.filter(Boolean); // Remove null values if no image exists
    }));

    const slideshow = new Slideshow(imageSources, ".slide-img");
    slideshow.start();
}

loadImages();
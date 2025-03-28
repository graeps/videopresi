import {Slideshow, playVideo} from './slideshow.js';

const basePath = "/static/images/";
const films = ["kizwebro", "haltbarmachen", "baecker"];
const numImages = 5;

const imageSources = films.map(film =>
    Array.from({length: numImages}, (_, i) => `${basePath}${film}/img${String(i + 1).padStart(2, '0')}.png`)
);

const slideshow = new Slideshow(imageSources, ".slide-img");
slideshow.start();
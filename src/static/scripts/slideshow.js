export class Slideshow {
    constructor(imageSources, selector, waitTime = 3000) {
        this.imageSources = imageSources;
        this.numberImg = this.imageSources.length
        this.selector = selector;
        this.waitTime = waitTime;
        this.currentIndex = 1;
        this.fadeTime = 3000;    // same value as in styles.css file!
        this.interval = this.numberImg * (2 * this.fadeTime + this.waitTime)
        this.imgs = document.querySelectorAll(this.selector);

        if (this.imgs.length === 0) {
            console.error(`No elements found for selector: ${this.selector}`);
        }
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async changeImage() {
        for (let i = 0; i < this.imgs.length; i++) {
            if (!this.imageSources[i]) {
                console.error(`No image sources found for index: ${i}`);
                continue;
            }

            this.imgs[i].style.opacity = "0"
            await this.sleep(this.fadeTime);
            this.imgs[i].src = this.imageSources[i][this.currentIndex];
            this.imgs[i].style.opacity = "1";
            await this.sleep(this.fadeTime + this.waitTime);
        }

        this.currentIndex = (this.currentIndex + 1) % this.imageSources[0].length;
    }

    start() {
        this.changeImage();  // Run once immediately
        setInterval(() => this.changeImage(), this.interval);
    }
}

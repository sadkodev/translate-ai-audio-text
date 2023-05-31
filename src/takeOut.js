import Tesseract from 'tesseract.js';

// eslint-disable-next-line require-jsdoc
export default async function getTextToImage(url) {
  try {
    const {
      data: {text},
    } = await Tesseract.recognize(url, 'eng', {logger: (m) => console.log(m)});
    return {text};
  } catch (error) {
    console.error(error);
    return '';
  }
}

function Exhibit(name, description) {
    this.name = name;
    this.description = description;
  }
  
  Exhibit.prototype.getName = function() {
    return this.name;
  };
  
  Exhibit.prototype.getDescription = function() {
    return this.description;
  };
  
  Exhibit.prototype.setName = function(name) {
    this.name = name;
  };
  
  Exhibit.prototype.setDescription = function(description) {
    this.description = description;
  };
  

  function Artwork(name, description, artist) {
    Exhibit.call(this, name, description);
    this.artist = artist;
  }
  
  Artwork.prototype = Object.create(Exhibit.prototype); 
  Artwork.prototype.constructor = Artwork;
  
  Artwork.prototype.getArtist = function() {
    return this.artist;
  };
  
  Artwork.prototype.setArtist = function(artist) {
    this.artist = artist;
  };
  
 
  var painting = new Artwork("The Starry Night", "A famous painting by Vincent van Gogh", "Vincent van Gogh");
  
  console.log(painting.getName()); 
  console.log(painting.getDescription()); 
  console.log(painting.getArtist()); 
  
  painting.setName("Starry Night"); 
  painting.setDescription("A masterpiece by Vincent van Gogh"); 
  painting.setArtist("Vincent Willem van Gogh");
  
  console.log(painting.getName()); 
  console.log(painting.getDescription()); 
  console.log(painting.getArtist()); 

  function descriptionDecorator(f) 
  {
    return function() {
      return `Description:` +  f.apply(this, arguments);
    }
  }

class Exhibit1 {
  constructor(name, description) {
    this.name = name;
    this.description = description;
  }

  getName() {
    return this.name;
  }

  getDescription() {
    return this.description;
  }

  setName(name) {
    this.name = name;
  }

  setDescription(description) {
    this.description = description;
  }
}

class Artwork1 extends Exhibit1 {
  constructor(name, description, artist) {
    super(name, description);
    this.artist = artist;
  }

  getArtist() {
    return this.artist;
  }

  setArtist(artist) {
    this.artist = artist;
  }
}

const painting1 = new Artwork("Sunflowers", "A series of paintings by Vincent van Gogh", "Vincent van Gogh");

console.log(painting1.getName()); 
painting1.getDescription = descriptionDecorator(painting1.getDescription);
console.log(painting1.getDescription());
console.log(painting1.getArtist());

painting1.setName(" Beautiful Sunflowers");
painting1.setDescription("Cool series of paintings by Vincent van Gogh");
painting1.setArtist("Vincent Willem van Gogh"); 

console.log(painting1.getName());
console.log(painting1.getDescription());
console.log(painting1.getArtist());
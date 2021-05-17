function loadDoc() {
    $.ajax({
  
           url: "movies.xml",
           dataType: "xml",
           success: function(data) {
              $("table").append('<tr><th>Title</th><th>Genre</th><th>Director</th><th>Cast</th><th>Short Description</th><th>IMDB-rating</th></tr>');
              $(data).find('movie').each(function(){
                  var title = $(this).find('title').text();
                  var genres = $(this).find('genre');
                  var genre = "";
                  $(genres).each(function(){
                      genre += $(this).text() + ",";
                  });
                  genre = genre.substr(0, genre.length-1);
                  var director = $(this).find('director').text();
                  var casts = $(this).find('cast').find('person');
                  var cast = "";
                  $(casts).each(function(){
                      cast += $(this).attr('name') + ",";
                  });
                  cast = cast.substr(0, cast.length-1);
                  console.debug(cast);
                  var shortDescription = $(this).find('imdb-info').find('synopsis').text();
                  var rating = $(this).find('imdb-info').find('score').text();
                  var info = '<tr><td>' + title +'</td><td>' + genre + '</td><td>' + director + '</td><td>' + cast + '</td><td>' + shortDescription + '</td><td>' + rating + '</td></tr>';
                  $("table").append(info);
              });
              
  
           },
           error: function() { alert("error loading file");  }
       });
  
  
  }
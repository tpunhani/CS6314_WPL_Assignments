import React, {Component} from 'react';
import Videos from './Components/videos';
import Search from './Components/Search';


class App extends Component {

  state = {
    videos: [],
    searchVideosFilter: '',
    filteredVideos: []
  }


  handleInput = (e) => {
    console.log(e.target.value)
    this.setState( {searchVideosFilter: e.target.value })
  }

  handleClick = () => {
    let filteredVideos = this.state.videos.filter((video) => {
      return video.title.toLowerCase().includes(this.state.searchVideosFilter.toLowerCase())
    });

    this.setState({ filteredVideos : filteredVideos })
  }



  componentDidMount() {
    fetch('http://127.0.0.1:5000/videos')
    .then(res => res.json())
    .then((data) => {
      this.setState( {videos: data })
      this.setState({ filteredVideos: data })
    })
    .catch(console.log)
  }

  render(){
    return (
      <div className="container">
      <Search handleInput={this.handleInput} handleClick={ this.handleClick }/>
      <Videos videos={this.state.filteredVideos} />
      </div>
    );
  }
}

export default App;

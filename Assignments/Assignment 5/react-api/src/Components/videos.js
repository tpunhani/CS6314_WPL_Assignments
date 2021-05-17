import React from 'react'

const Videos = (props) => {
    return(
        <>
            {
                props.videos.map((video) => (
                    <div className="card" key={video._id}>
                        <div className="card-body">
                            <h5 className="card-title">{video.title}</h5>
                            <h6 className="subtitle md-2 text-muted">{video.genre}</h6>
                            <p className="card-text">{video.description}</p>
                    </div>
                </div>
                
            ))}
        </>
    );
}

export default Videos
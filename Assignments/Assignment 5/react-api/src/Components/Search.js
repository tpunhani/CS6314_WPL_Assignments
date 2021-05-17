import React from 'react'

function Search(props) {
    return (
        <div>
            <nav className="navbar navbar-dark bg-dark justify-content-between">
                <a className="navbar-brand p-3">Video List</a>
                <span>
                    <input className="mr-sm-2 inputSearch p-1" onChange={props.handleInput} type="search" placeholder="Search" aria-label="Search" />
                    <button className="btn btn-primary m-3" onClick={props.handleClick}>Search</button>
                    </span>
            </nav>

        </div>
    )
}

export default Search

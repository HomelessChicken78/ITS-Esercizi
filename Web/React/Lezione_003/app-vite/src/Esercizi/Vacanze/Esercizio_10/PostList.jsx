const PostList = (props) => {
    return (
        <div className="my-4">

            {
                props.posts.map((post, id) => {
                    return (
                        <div className="card my-2" style={{ width: '18rem;' }} key={id}>
                            <div className="card-body">
                                <h5 className="card-title">{post.Titolo}</h5>
                                <p className="card-text">{post.Contenuto}</p>
                            </div>
                        </div>
                    )
                })
            }
        </div>
    )
}

export default PostList
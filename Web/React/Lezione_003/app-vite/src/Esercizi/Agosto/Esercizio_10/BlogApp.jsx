import { useState } from "react"
import PostForm from "./PostForm"
import PostList from "./PostList"

const BlogApp = () => {
    const [posts, setPosts] = useState([])

    const aggiungiPost = (post) => {
        setPosts([
            ...posts,
            post
        ])
        console.log(posts)
    }


    return (
        <>
            <PostForm>{aggiungiPost}</PostForm>
            <PostList posts={posts}/>
        </>
    )
}

export default BlogApp

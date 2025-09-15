import { useRef } from "react";

const PostForm = (props) => {
    const title = useRef("")
    const content = useRef("")

    return (
        <form onSubmit={(e) => {
            e.preventDefault();
            props.children({
                Titolo : title.current.value,
                Contenuto: content.current.value
            })
        }}>
            <input type="text" name="Titolo" ref={title} placeholder="Titolo del post"/>
            <input type="text" name="Contenuto" ref={content} placeholder="Contenuto..."/>
            <button type="submit" className="btn btn-outline-secondary mx-2">Posta</button>
        </form>
    )
}

export default PostForm

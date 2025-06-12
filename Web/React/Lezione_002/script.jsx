const elementRoot = document.querySelector("#root");
const root = ReactDOM.createRoot(elementRoot);

const App = ({children}) => {
    console.log(children);
    return (
        <main>
            <h1>Primo componente</h1>
            {children}
        </main>
    )
}

const List = function () {
    return (
        <ul>
            <li>PHP</li>
            <li>JS</li>
            <li>Python</li>
        </ul>
    )
}

root.render(
    <>
        <App>
            <h2>Lista competenza</h2>
            <List></List>
        </App>
    </>
)
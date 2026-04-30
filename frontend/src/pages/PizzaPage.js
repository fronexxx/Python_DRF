import Chat from "../components/Chat";
import PizzaForm from "../components/PizzaForm";
import PizzasComponent from "../components/PizzasComponent";

const PizzaPage = () => {
    return (
        <div>
            <PizzaForm/>
            <hr/>
            <PizzasComponent/>
            <hr/>
            <Chat/>
        </div>
    );
};

export default PizzaPage;
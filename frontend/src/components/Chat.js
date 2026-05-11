import {useEffect, useRef, useState} from "react";
import {socketService} from "../services/socketService";

const Chat = () => {
    const [room, setRoom] = useState(null);
    const [socketClient, setSocketClient] = useState(null);
    const [messages, setMessages] = useState([]);
    const [targetUser, setTargetUser] = useState(null);
    const roomInput = useRef();

    useEffect(() => {
        if (room) {
            socketInit(room).then(client => setSocketClient(client))
        }
    }, [room]);

    const socketInit = async (room) => {
        const {chat} = await socketService();
        const client = await chat(room);

        client.onopen = () => {
            console.log('chat socket connected');
        }

        client.onmessage = ({data}) => {
            const {message, user} = JSON.parse(data.toString());
            if (user) {
                const [userId, username] = user.split('_');
                setMessages(prevState => [...prevState, {userId, username, message}]);
            } else {
                setMessages(prevState => [...prevState, {message, user}]);
            }
        };

        return client

    }
    const roomHandler = () => {
        setRoom(roomInput.current.value)
    }
    const EnterHandler = (e) => {
        if (e.key === 'Enter') {
            socketClient.send(JSON.stringify({
                data: !targetUser ? {text: e.target.value}: {text: `Private ${e.target.value}`, userId: targetUser},
                action: !targetUser ? 'send_message' : 'send_private_message',
                request_id: new Date().getTime()
            }))
            e.target.value = ''
        }
    }
    return (
        !room
            ?
            <div>
                <input type="text" ref={roomInput}/>
                <button onClick={roomHandler}>Go to room</button>
            </div>
            :
            <div>
                {messages.map(msg =>
                    <div>
                        <span onClick={() => {
                            if (!targetUser) {
                                setTargetUser(msg.userId);
                            }else {
                                setTargetUser(null)
                            }
                            console.log(targetUser);
                        }}>{msg.username}</span>: {msg.message}
                    </div>)}
                <input type="text" onKeyDown={EnterHandler}/>
            </div>
    );
};

export default Chat;
    
import * as React from 'react';
import { Socket } from './Socket';



import { MessageForm } from './MessageForm';


export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'data': '',
        };
    }
    
 
    componentDidMount() {
        Socket.on('message received', (data) => {
            console.log("Content recieved message");
            this.setState({
                'number_received': data['message']
            });
        });
    }

    render() {
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '1000px', border: '1px solid #000'}}>
        <h1>ChatBot</h1>
        <body>
        </body>
        </div>;
    }
}
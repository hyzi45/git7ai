import gradio as gr

todos = []

def add_todo(todo):
    todos.append(todo)
    # 번호를 붙여서 출력
    return "\n".join([f"{i+1}. {item}" for i, item in enumerate(todos)])

def delete_todo(index):
    try:
        idx = int(index) - 1
        if 0 <= idx < len(todos):
            todos.pop(idx)
        # 번호를 붙여서 출력
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(todos)])
    except:
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(todos)])

with gr.Blocks() as app:
    gr.Markdown("## Todo List Manager")
    with gr.Row():
        todo_input = gr.Textbox(label="Add Todo")
        add_btn = gr.Button("Add")
    with gr.Row():
        delete_input = gr.Number(label="Delete index")
        delete_btn = gr.Button("Delete")
    output = gr.Textbox(label="Todo List")
    add_btn.click(add_todo, inputs=todo_input, outputs=output)
    delete_btn.click(delete_todo, inputs=delete_input, outputs=output)

app.launch()
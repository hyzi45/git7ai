import gradio as gr

todos = []

def add_todo(todo):
    if todo.strip():
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

with gr.Blocks(theme=gr.themes.Soft()) as app:  # 테마 적용
    gr.Markdown("## Todo List Manager")
    with gr.Row():
        todo_input = gr.Textbox(label="Add Todo", placeholder="Enter a new task")
        add_btn = gr.Button("Add", variant="primary")  # 버튼 스타일 개선
    with gr.Row():
        delete_input = gr.Number(label="Delete index")
        delete_btn = gr.Button("Delete", variant="secondary")  # 버튼 스타일 개선
    output = gr.Textbox(label="Todo List")
    add_btn.click(add_todo, inputs=todo_input, outputs=output)
    delete_btn.click(delete_todo, inputs=delete_input, outputs=output)
    gr.Examples(
        examples=[["Buy groceries"], ["Call mom"], ["Read a book"]],
        inputs=todo_input
    )  # 예제 입력 추가

app.launch()
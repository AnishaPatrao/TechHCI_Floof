//
//  ContentView.swift
//  FloofMonitor
//
//  Created by Anisha Patrao on 22/03/2022.
//

import SwiftUI

struct Course: Hashable, Codable{
    let name: String
    let image: String
}

class ViewModel: ObservableObject{
    func apiCall(status: Int){
        guard let url = URL(string:"http://groupb.local:5000/api/floof-sad/" + String(status)) else {
            return
        }
        
        var request = URLRequest(url: url)
        
        //method, body, headers
        request.httpMethod = "GET"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        //Make the request
        let task = URLSession.shared.dataTask(with: request){data, _, error in
            guard let data = data, error == nil else {
                return
            }
            
            do{
                let response = try JSONSerialization.jsonObject(with: data, options: .allowFragments)
                print("Success: \(response)")
            }
            catch{
                print("error: \(error)")
            }
        }
        task.resume()
    }
}

struct ContentView: View {
    var body: some View {
        
        VStack{
            
            Button("Welcome to Play Zone!!"){
                let viewModel = ViewModel()
                viewModel.apiCall(status: 1)
            }
            .padding()
            
            Button("Your high score is 1400"){
                let viewModel = ViewModel()
                viewModel.apiCall(status: 0)
            }
            
        }
        //to detect when the app is opened or goes into the background
        .onReceive(NotificationCenter.default.publisher(for: UIApplication.didEnterBackgroundNotification), perform: { output in
            let viewModel = ViewModel()
            viewModel.apiCall(status: 0)
        })
        //to detect when the app is opened or comes into the foregroud
        .onReceive(NotificationCenter.default.publisher(for: UIApplication.didBecomeActiveNotification), perform: { output in
            let viewModel = ViewModel()
            viewModel.apiCall(status: 1)
        })
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


